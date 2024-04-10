import ROOT

class HistogramGenerator:
    def __init__(self, name, title, num_bins, min_range, max_range):
        self.name = name
        self.title = title
        self.num_bins = num_bins
        self.min_range = min_range
        self.max_range = max_range
        self.hist = ROOT.TH1F(name, title, num_bins, min_range, max_range)

    def fill_histogram(self, data):
        self.hist.FillN(len(data), ROOT.AddressOf(data), np.ones_like(data))

    def set_titles(self, x_title, y_title):
        self.hist.GetXaxis().SetTitle(x_title)
        self.hist.GetYaxis().SetTitle(y_title)

    def set_tick_marks(self):
        self.hist.GetXaxis().SetTickx()
        self.hist.GetYaxis().SetTicky()

    def set_fill_color(self, color):
        self.hist.SetFillColor(color)

    def set_title_sizes(self, size):
        self.hist.GetXaxis().SetTitleSize(size)
        self.hist.GetYaxis().SetTitleSize(size)

    def draw_histogram(self):
        canvas = ROOT.TCanvas()
        self.hist.Draw()
        legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        legend.AddEntry(self.hist, self.title, "f")
        legend.Draw()
        canvas.Draw()

def generate_data(mean, std_dev, num_samples):
    return np.random.normal(mean, std_dev, num_samples)

def main():
    mean = 10
    std_dev = 3
    num_samples = 10000

    data = generate_data(mean, std_dev, num_samples)

    hist_generator = HistogramGenerator("hist", "Histogram", 100, 0, 20)

    hist_generator.hist.FillN(len(data), ROOT.AddressOf(data), np.ones_like(data))

    hist_generator.set_titles("X Axis", "Y Axis")
    hist_generator.set_tick_marks()
    hist_generator.set_fill_color(ROOT.kPink)
    hist_generator.set_title_sizes(0.5)
    hist_generator.draw_histogram()

if __name__ == "__main__":
    ROOT.gROOT.SetBatch(True)
    main()



