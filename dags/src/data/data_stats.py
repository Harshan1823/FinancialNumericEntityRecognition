import tensorflow_data_validation as tfdv

# Assume you have already generated the statistics and stored in train_stats
train_stats = tfdv.generate_statistics_from_csv(data_location='train.csv')

# Now, let's save the statistics to a .pbtxt file
tfdv.write_stats_text(statistics=train_stats, output_path='train_stats.pbtxt')


def data_stats(ROOT_FOLDER, FILE):
    pass
