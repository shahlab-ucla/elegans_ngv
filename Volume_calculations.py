from scipy.spatial import ConvexHull
import numpy as np
import matplotlib.pyplot as plt
import pickle
#import coordinate pickle file from Cell_cycle.ipynb (jupyter cannot handle ConvexHull due to memory constraints)

with open('coordinates.pickle', 'rb') as file:
    fullcoordlist = pickle.load(file)
with open('names.pickle', 'rb') as file:
    fullnamelist = pickle.load(file)
print(len(fullnamelist))
labels = ['N2','CB4856','JIM113','MY23','DL238','ECA36','JU2001','XZ1516']
all_volumes = []
volume_strain_dict = {}
count = 0
for n in fullcoordlist:
    strain_volume = []
    for emb in n:
        coords = np.array(list(emb.values()))
        v = ConvexHull(coords)
        if v.volume < 50000:
            strain_volume.append(v.volume/1000)
            volume_strain_dict[fullnamelist[count]] = v.volume
            count += 1
        else:
            print(fullnamelist[count])
    all_volumes.append(strain_volume)
    
with open('volumes.pickle', 'wb') as file:
    pickle.dump(volume_strain_dict, file)
plt.figure()

# --- boxplot ---
bp = plt.boxplot(all_volumes, positions=range(1, len(labels)+1), widths=0.5)

# --- scatter ---
for i, vols in enumerate(all_volumes):
    x = np.random.normal(i+1, 0.08, size=len(vols))  # shift to align with boxplot
    plt.scatter(x, vols)

plt.xticks(range(1, len(labels)+1), labels)
#plt.ylim(0,25000)
plt.show()

for i, label in enumerate(labels):
    median = bp['medians'][i].get_ydata()[0]
    q1 = bp['boxes'][i].get_ydata()[1]
    q3 = bp['boxes'][i].get_ydata()[2]
    iqd = q3 - q1
    whisker_low = bp['whiskers'][2*i].get_ydata()[1]
    whisker_high = bp['whiskers'][2*i+1].get_ydata()[1]
    print(f"{label}: median={median:.2f}, Q1={q1:.2f}, Q3={q3:.2f}, "
          f"whisker_low={whisker_low:.2f}, whisker_high={whisker_high:.2f}, " f"IQD={iqd:.2f}")
    
print(f"{'Strain':<10} {'Median':<10} {'IQR':<10} {'Pairs':<10}")

for label, vals in zip(labels, all_volumes):
    median = np.median(vals)
    q1 = np.percentile(vals, 25)
    q3 = np.percentile(vals, 75)
    iqr = q3 - q1
    pairs = len(vals)

    print(f"{label:<10} {median:<10.2f} {iqr:<10.2f} {pairs:<10}")