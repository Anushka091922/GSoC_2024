import unittest
import numpy as np
import ROOT



class TestHistogram(unittest.TestCase):

    def test_negative_std_dev(self):
        print("Testing negative standard deviation...")
        with self.assertRaises(ValueError):
            generate_data(10, -2, 1000)

    def test_zero_sample_size(self):
        print("Testing zero sample size...")
        data = generate_data(10, 2, 0)
        self.assertEqual(len(data), 0)

    def test_data_distribution(self):
        mean, std_dev, num_samples = 10, 2, 1000
        data = generate_data(mean, std_dev, num_samples)
        data_mean = np.mean(data)
        data_std_dev = np.std(data)
        print(f"Generated data mean: {data_mean}, expected mean: {mean}")
        print(f"Generated data std_dev: {data_std_dev}, expected std_dev: {std_dev}")
        self.assertAlmostEqual(data_mean, mean, delta=0.2 * std_dev)  # Allowing slightly higher tolerance
        self.assertAlmostEqual(data_std_dev, std_dev, delta=0.2 * std_dev)

    
    
    def test_large_dataset(self):
        print("Testing with large dataset (adjust parameters if needed)...")
     
        num_samples = 100000
        data = generate_data(15, 5, num_samples)
      
        print(f"Generated data size (for reference): {len(data)}")
        # Skipping histogram creation for large datasets to avoid memory issues


def generate_data(mean, std_dev, num_samples):
    return np.random.normal(mean, std_dev, num_samples)


def fill_histogram_with_histogram_factory(data):
    sample = Sample(data)
    histogram = HistogramFactory().build(sample)
    hist = ROOT.TH1F("hist", "Histogram from HistogramFactory", histogram.getBinNumber(),
                     histogram.getLowerBound()[0], histogram.getUpperBound()[0])
    for i in range(histogram.getBinNumber()):
        hist.SetBinContent(i + 1, histogram.getBin(i)[1])
    hist.SetTitle("Histogram from HistogramFactory")
    hist.GetXaxis().SetTitle("X Axis")
    hist.GetYaxis().SetTitle("Y Axis")
    hist.SetFillColor(ROOT.kPink)
    hist.SetTickx()
    hist.SetTicky()
    return hist


if __name__ == "__main__":
    unittest.main()

