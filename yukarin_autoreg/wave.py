from pathlib import Path

import librosa
import numpy as np

from yukarin_autoreg.sampling_data import SamplingData


class Wave(object):
    def __init__(
            self,
            wave: np.ndarray,
            sampling_rate: int,
    ) -> None:
        self.wave = wave
        self.sampling_rate = sampling_rate

    @staticmethod
    def load(path: Path, sampling_rate: int = None, dtype=np.float32):
        if path.suffix == '.npy' or path.suffix == '.npz':
            a = SamplingData.load(path)
            return Wave(wave=np.squeeze(a.array), sampling_rate=a.rate)
        else:
            wave, sampling_rate = librosa.core.load(str(path), sr=sampling_rate, dtype=dtype)
            return Wave(wave=wave, sampling_rate=sampling_rate)

    def save(self, path: Path):
        librosa.output.write_wav(str(path), y=self.wave, sr=self.sampling_rate)
