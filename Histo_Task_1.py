import numpy as np
import ROOT
import time


class HistogramPlotter:
    def __init__(self, title, num_bins, x_min, x_max):
        self.histogram = ROOT.TH1F("histogram", title, num_bins, x_min, x_max)


    def fill_histogram(self, data):
        self.histogram.FillN(len(data), data.astype(np.double), np.ones(len(data), dtype=np.double))


    def draw_histogram(self, wait_time=30):
        canvas = ROOT.TCanvas("canvas", "Histogram", 800, 600)
        self.histogram.Draw()
        canvas.Draw()
        time.sleep(wait_time)


class NormalDistributionPlotter(HistogramPlotter):
    def __init__(self, mean, std_dev, num_samples):
        super().__init__("Normal Distribution", 100, 0, 20)
        self.data = np.maximum(0, np.round(np.random.normal(mean, std_dev, num_samples))).astype(int)


    def fill_histogram(self):
        super().fill_histogram(self.data)


def generate_and_plot_normal_distribution(mean, std_dev, num_samples):
    plotter = NormalDistributionPlotter(mean, std_dev, num_samples)
    plotter.fill_histogram()
    plotter.draw_histogram()
generate_and_plot_normal_distribution(10, 3, 10000)




