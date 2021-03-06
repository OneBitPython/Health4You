"""This data was scraped from this website : https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-of-leisure-and-routine-activities
using selenium. The data contains calories burned by doing different exercises."""

all_activities = {
    "Weight Lifting: general": [90, 108, 126],
    "Aerobics: water": [120, 144, 168],
    "Stretching, Hatha Yoga": [120, 144, 168],
    "Calisthenics: moderate": [135, 162, 189],
    "Aerobics: low impact": [165, 198, 231],
    "Stair Step Machine: general": [180, 216, 252],
    "Weight Lifting: vigorous": [180, 216, 252],
    "Aerobics, Step: low impact": [210, 252, 294],
    "Aerobics: high impact": [210, 252, 294],
    "Bicycling, Stationary: moderate": [210, 252, 294],
    "Rowing, Stationary: moderate": [210, 252, 294],
    "Calisthenics: vigorous": [240, 306, 336],
    "Rowing, Stationary: vigorous": [255, 369, 440],
    "Elliptical Trainer: general": [270, 324, 378],
    "Ski Machine: general": [285, 342, 399],
    "Aerobics, Step: high impact": [300, 360, 420],
    "Bicycling, Stationary: vigorous": [315, 278, 441],
    "Dancing: slow, waltz, foxtrot": [90, 108, 125],
    "Frisbee": [85, 105, 125],
    "Volleyball: non-competitive, general play": [90, 108, 126],
    "Water Volleyball": [90, 108, 126],
    "Golf: using cart": [105, 126, 147],
    "Gymnastics: general": [120, 144, 168],
    "Horseback Riding: general": [57, 70, 84],
    "Tai Chi": [120, 144, 168],
    "Volleyball: competitive, gymnasium play": [226, 281, 335],
    "Walking: 3.5 mph (17 min/mi)": [107, 133, 159],
    "Badminton: general": [114, 141, 168],
    "Walking: 4 mph (15 min/mi)": [135, 175, 189],
    "Kayaking": [150, 180, 210],
    "Skateboarding": [150, 180, 210],
    "Softball: general play": [141, 180, 210],
    "Whitewater: rafting, kayaking": [150, 180, 210],
    "Dancing: disco, ballroom, square": [165, 198, 231],
    "Golf: carrying clubs": [165, 198, 231],
    "Dancing: Fast, ballet, twist": [180, 216, 252],
    "Hiking: cross-country": [170, 216, 252],
    "Skiing: downhill": [180, 216, 252],
    "Swimming: general": [180, 216, 252],
    "Walk/Jog: jog <10 min.": [180, 216, 252],
    "Water Skiing": [180, 216, 252],
    "Wrestling": [180, 216, 252],
    "Basketball: wheelchair": [195, 234, 273],
    "Ice Skating: general": [210, 252, 294],
    "Racquetball: casual, general": [210, 252, 293],
    "Rollerblading/skating (Casual)": [311, 386, 461],
    "Rollerblading/skating (Fast)": [340, 421, 503],
    "Scuba or skin diving": [210, 252, 294],
    "Sledding, luge, toboggan": [199, 247, 294],
    "Soccer: general": [210, 252, 294],
    "Tennis: general": [210, 252, 294],
    "Basketball: playing a game": [240, 288, 336],
    "Bicycling: 12-13.9 mph": [240, 288, 336],
    "Football: touch, flag, general": [240, 288, 336],
    "Hockey: field & ice": [240, 288, 336],
    "Rock Climbing: rappelling": [227, 282, 336],
    "Running: 5 mph (12 min/mile)": [240, 288, 336],
    "Skiing: cross-country": [198, 246, 293],
    "Snow Shoeing": [240, 288, 336],
    "Volleyball: beach": [240, 288, 336],
    "Bicycling: BMX or mountain": [255, 306, 357],
    "Boxing: sparring": [270, 324, 378],
    "Football: competitive": [270, 324, 378],
    "Running: cross-country": [255, 316, 377],
    "Bicycling: 14-15.9 mph": [300, 360, 420],
    "Martial Arts: judo, karate, kickbox": [300, 360, 420],
    "Racquetball: competitive": [300, 360, 420],
    "Rope Jumping (Fast)": [340, 421, 503],
    "Rope Jumping (Slow)": [226, 281, 335],
    "Running: 6 mph (10 min/mile)": [495, 360, 420],
    "Swimming: laps, vigorous": [300, 360, 420],
    "Water Polo": [300, 360, 420],
    "Rock Climbing: ascending": [226, 281, 335],
    "Bicycling: 16-19 mph": [360, 432, 504],
    "Handball: general": [360, 432, 504],
    "Running: 7.5 mph (8 min/mile)": [375, 450, 525],
    "Bicycling: > 20 mph": [495, 594, 693],
    "Running: 10 mph (6 min/mile)": [453, 562, 671],
    "Raking lawn": [120, 144, 168],
    "Gardening: general": [135, 162, 189],
    "Mowing lawn: push, power": [135, 162, 189],
    "Operate Snow Blower: walking": [135, 162, 189],
    "Carrying & stacking wood": [142, 176, 210],
    "Mowing Lawn: push, hand": [165, 198, 231],
    "Chopping & splitting wood": [180, 216, 252],
}
