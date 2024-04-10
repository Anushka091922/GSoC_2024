import ROOT
import time
import numpy as np

def read_data_from_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:  #this will  check if there is any empty line in the file
                value = float(line)
                data.append(value)
    return np.array(data)

def example():
    # Read data from file and convert to NumPy array
    file_data = read_data_from_file("dataset.txt")
    
    # Generating the normally distributed data based on file data
    mean = np.mean(file_data)
    std_dev = np.std(file_data)
    normal_data = np.random.normal(mean, std_dev, len(file_data))
    
    # Creating the ROOT histogram
    hist = ROOT.TH1F("hist", "Histogram", 100, min(file_data), max(file_data))
    
    # Fill the histogram with data
    for value in normal_data:
        hist.Fill(value)
    
   
    max_bin_content = hist.GetMaximum()
    
   
    max_std_dev_bins = []
    for i in range(1, hist.GetNbinsX() + 1):
        if hist.GetBinContent(i) == max_bin_content:
            max_std_dev_bins.append(hist.GetBinCenter(i))
    
    # Addding grid to the plot
    ROOT.gStyle.SetPadGridX(1)
    ROOT.gStyle.SetPadGridY(1)
    
    # Drawing histogram
    hist.GetXaxis().SetTitle("X Axis")
    hist.GetYaxis().SetTitle("Y Axis")
    hist.SetLineColor(ROOT.kBlue)
    hist.Draw()
    
    # Drawing legend
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(hist, "Normal Distribution", "l")
    legend.Draw()
    
    # Mark point of maximum standard deviation
    max_std_dev_marker = ROOT.TMarker(max_std_dev_bins[0], max_bin_content, 20)
    max_std_dev_marker.SetMarkerColor(ROOT.kRed)
    max_std_dev_marker.Draw()
    
    c1 = ROOT.TCanvas()
    hist.Draw()
    
    time.sleep(60)  

if __name__ == "__main__":
    example()
