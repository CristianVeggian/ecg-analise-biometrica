import numpy as np
from scipy.signal import medfilt, butter, filtfilt
from biosppy.signals import ecg
import tsfel
import pandas as pd
from scipy.signal import find_peaks
import os

pasta = 'features'
arquivos = os.listdir(pasta)
fs = 500

cfg = tsfel.get_features_by_domain()

for id, arquivo in enumerate(arquivos):

    dados = np.loadtxt(os.path.join(pasta, arquivo))

    tempo = [i / fs for i in range(len(dados))]

    ecg_raw = dados.astype(np.float64)

    janela_1 = int(0.2 * fs) # remover o complexo QRS
    ecg_sem_qrs = medfilt(ecg_raw, kernel_size=janela_1 if janela_1 % 2 == 1 else janela_1 + 1)

    # remover a onda T
    janela_2 = int(0.6 * fs)
    baseline = medfilt(ecg_sem_qrs, kernel_size=janela_2 if janela_2 % 2 == 1 else janela_2 + 1)

    ecg_corrigido = ecg_raw - baseline

    nyq = 0.5 * fs
    low = 0.5 / nyq
    high = 50.0 / nyq
    b, a = butter(4, [low, high], btype='band')
    ecg_filtrado = filtfilt(b, a, ecg_corrigido)

    #extrai características do sinal
    ecg_dados = ecg.ecg(dados, sampling_rate=fs, show=False)

    pre_pico = 0.2
    pos_pico = 0.4

    batimentos, picos = ecg.extract_heartbeats(ecg_filtrado, ecg_dados['rpeaks'], fs, pre_pico, pos_pico)

    if arquivo.endswith("1.txt"):
        estado = 'repouso'
    else:
        estado = 'atividade'

    for batimento in batimentos:
        
        ecg_features = []

        df = pd.DataFrame(batimento)
        features = tsfel.time_series_features_extractor(cfg, df, fs=fs, verbose=False, n_jobs=-1)
        picos, _ = find_peaks(batimento)
        vales, _ = find_peaks(-batimento)

        picos, _ = find_peaks(batimento)
        vales, _ = find_peaks(-batimento)

        if len(picos) > 0 and len(vales) > 0:
            R = batimento[picos].max()
            S = batimento[vales].min()

            idx_R = np.argmax(batimento[picos])
            idx_S = np.argmin(batimento[vales])
            pos_R = picos[idx_R]
            pos_S = vales[idx_S]

            rs_ratio = R / abs(S)

            qrs_duration = abs(pos_S - pos_R) / fs   # em segundos
            slope_rs = (R - S) / (abs(pos_S - pos_R) + 1e-6)
            area_qrs = np.trapezoid(batimento[pos_R:pos_S])

        else:
            R, S, rs_ratio, qrs_duration, slope_rs, area_qrs = [np.nan]*6

        ecg_features.append({
            "ID": (id // 2) + 1,
            "Estado": estado,
            "R_amplitude": R,
            "S_amplitude": S,
            "RS_ratio": rs_ratio,
            "QRS_duration_s": qrs_duration,
            "Slope_RS": slope_rs,
            "Area_QRS": area_qrs,
            **features.iloc[0].to_dict()
        })

        ecg_features_df = pd.DataFrame(ecg_features)

        ecg_features_df.to_csv('features.csv', mode='a', header=False, index=False)