import numpy as np
import ROOT
import openturns as ot


def generate_data(mean, std_dev, num_samples):
    return np.random.normal(mean, std_dev, num_samples)


def fill_histogram_with_histogram_factory(data):
    sample = ot.Sample(data)
    histogram = ot.HistogramFactory().build(sample)
    hist = ROOT.TH1F("hist", "Histogram from HistogramFactory", histogram.getBinNumber(),histogram.getLowerBound()[0],histogram.getUpperBound()[0])
    for i in range(histogram.getBinNumber()):
        hist.SetBinContent(i + 1, histogram.getBin(i)[1])
    hist.SetTitle("Histogram from HistogramFactory")
    hist.GetXaxis().SetTitle("X Axis")
    hist.GetYaxis().SetTitle("Y Axis")
    hist.SetFillColor(ROOT.kPink)
    hist.SetTickx()
    hist.SetTicky()


    canvas = ROOT.TCanvas()
    hist.Draw()
    canvas.Draw()


def main():
    mean = 10
    std_dev = 3
    num_samples = 10000


    data = generate_data(mean, std_dev, num_samples)
    fill_histogram_with_histogram_factory(data)


if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()
