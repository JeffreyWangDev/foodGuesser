# Download the data from the USDA website and generate the data.json file 
# Put it in the /data folder

food_ids = [
    329648, 329665, 329668, 329671, 329677, 329680, 329683, 329690, 329692, 329693, 329700, 329703, 329707, 329712, 329716, 329717, 329721, 329722, 329728, 329731, 329732, 329735, 329736, 329738, 329740, 329741, 329743, 329745, 329750, 329751, 329752, 329753, 329754, 329755, 329756, 329759, 329763, 329764, 329766, 329769, 329770, 329771, 329772, 329774, 329776, 329779, 329780, 329782, 329784, 329785, 329787, 329789, 329790, 329791, 329794, 329795, 329797, 329799, 329800, 329801, 329803, 329804, 329805, 329807, 329811, 329812, 329813, 329814, 329815, 329816, 329818, 329819, 329820, 329822, 329823, 329824, 329826, 329828, 329830, 329831, 329832, 329834, 329835, 329837, 329838, 329839, 329840, 329841, 329842, 329845, 329847, 329848, 329849, 329850, 329851, 329852, 329853, 329854, 329857, 329858, 329860, 329862, 329863, 329864, 329867, 329868, 329869, 329871, 329873, 329875, 329876, 329877, 329878, 329881, 329883, 329886, 329887, 329888, 329890, 329891, 329892, 329893, 329894, 329895, 329896, 329898, 329899, 329900, 329901, 329902, 329903, 329904, 329905, 329906, 329907, 329908, 329909, 329910, 329912, 329913, 329914, 329915, 329917, 329918, 329920, 329921, 329922, 329923, 329924, 329925, 329926, 329928, 329930, 329931, 329932, 329933, 329935, 329936, 329937, 329938, 329940, 329941, 329942, 329944, 329945, 329946, 329947, 329949, 329950, 329951, 329952, 329953, 329955, 329956, 329957, 329958, 329959, 329960, 329961, 329962, 329963, 329964, 329965, 329966, 329967, 329968, 329971, 329973, 329974, 329975, 329976, 329977, 329978, 329979, 329981, 329982, 329983, 329984, 329985, 329986, 329987, 329988, 329989, 329990, 329991, 329992, 329993, 329994, 329995, 329996, 329997, 329999, 330000, 330001, 330002, 330003, 330004, 330005, 330006, 330007, 330008, 330009, 330010, 330011, 330012, 330013, 330014, 330015, 330016, 330017, 330018, 330019, 330020, 330021, 330022, 330023, 330024, 330025, 330026, 330027, 330028, 330029, 330030, 330031, 330033, 330034, 330035, 330036, 330037, 330038, 330039, 330040, 330041, 330042, 330043, 330044, 330045, 330047, 330048, 330050, 330051, 330052, 330053, 330054, 330055, 330056, 330057, 330058, 330059, 330061, 330062, 330063, 330064, 330065, 330066, 330067, 330068, 330069, 330070, 330071, 330072, 330073, 330074, 330075, 330076, 330077, 330078, 330079, 330080, 330081, 330082, 330083, 330084, 330085, 330086, 330087, 330088, 330089, 330090, 330091, 330092, 330093, 330094, 330095, 330096, 330097, 330098, 330099, 330100, 330101, 330102, 330103, 330104, 330105, 330106, 330107, 330108, 330109, 330110, 330111, 330112, 330113, 330114, 330115, 330116, 330117, 330118, 330119, 330120, 330121, 330122, 330123, 330124, 330125, 330126, 330127, 330128, 330129, 330130, 330131, 330132, 330133, 330134, 330135, 330136, 330137, 330138, 330139, 330140, 330141, 330142, 330143, 330144, 330145, 330146, 330147, 330148, 330149, 330150, 330151, 330152, 330153, 330154, 330155, 330156, 330157, 330158, 330159, 330160, 330161, 330162, 330163, 330164, 330165, 330166, 330167, 330168, 330169, 330170, 330171, 330172, 330173, 330174, 330175, 330176, 330177, 330178, 330179, 330180, 330181, 330182, 330183, 330184, 330185, 330186, 330187, 330188, 330189, 330190, 330191, 330192, 330193, 330194, 330195, 330196, 330197, 330198, 330199, 330200, 330201, 330202, 330203, 330204, 330205, 330206, 330207, 330208, 330209, 330210, 330211, 330212, 330213, 330214, 330215, 330216, 330217, 330218, 330219, 330220, 330221, 330222, 330223, 330224, 330225, 330226, 330227, 330228, 330229, 330230, 330231, 330232, 330233, 330234, 330235, 330236, 330237, 330238, 330239, 330240, 330241, 330242, 330243, 330244, 330245, 330246, 330247, 330248, 330249, 330250, 330251, 330252, 330253, 330254, 330255, 330256, 330257, 330258, 330259, 330260, 330261, 330262, 330263, 330264, 330265, 330266, 330267, 330268, 330269, 330270, 330271, 330272, 330273, 330274, 330275, 330276, 330277, 330278, 330279, 330280, 330281, 330282, 330283, 330284, 330285, 330286, 330287, 330288, 330289, 330290, 330291, 330292, 330293, 330294, 330295, 330296, 330297, 330298, 330299, 330300, 330301, 330302, 330303, 330304, 330305, 330306, 330307, 330308, 330309, 330310, 330311, 330312, 330313, 330314, 330315, 330316, 330317, 330318, 330319, 330320, 330321, 330322, 330323, 330324, 330325, 330326, 330327, 330328, 330329, 330330, 330331, 330332, 330333, 330334, 330335, 330336, 330337, 330338, 330339, 330340, 330341, 330342, 330343, 330344, 330345, 330346, 330347, 330348, 330349, 330350, 330351, 330352, 330353, 330354, 330355, 330356, 330357, 330358, 330359, 330360, 330361, 330362, 330363, 330364, 330365, 330366, 330367, 330368, 330369, 330370, 330371, 330372, 330373, 330374, 330375, 330376, 330377, 330378, 330379, 330380, 330381, 330382, 330383, 330384, 330385, 330386, 330387, 330388, 330389, 330390, 330391, 330392, 330393, 330394, 330395, 330396, 330397, 330398, 330399, 330400, 330401, 330402, 330403, 330404, 330405, 330406, 330407]
new_ids = []

for food_id in food_ids:
    new_ids.append(int("1"+str(food_id)))
    new_ids.append(int("2"+str(food_id)))

fdc_id_set = set(new_ids)
fdc_ids = new_ids
import pandas as pd
import json
import numpy as np

df = pd.read_csv("data/food.csv",low_memory=False)

df2 = pd.read_csv("data/branded_food.csv",low_memory=False)

df3 = pd.read_csv("data/food_nutrient.csv",low_memory=False)

df4 = pd.read_csv("data/nutrient.csv",low_memory=False)

filtered_df = df[df['fdc_id'].isin(fdc_ids)]

fdc_id_values = filtered_df['fdc_id'].values
description_values = filtered_df['description'].values

end = []

for fdc_id, description in zip(fdc_id_values, description_values):
    if len(description) > 50:
        continue    
    ing = df2.loc[df2['fdc_id'] == fdc_id]["ingredients"]
    
    neu = df3.loc[df3['fdc_id'] == fdc_id].values.tolist()
    
    end.append((int(fdc_id), description, list(ing.values), neu))
print(len(end))

with open('data.json', 'w') as f:
    json.dump(end, f)