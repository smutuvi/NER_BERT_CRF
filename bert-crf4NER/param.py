class PARAM(object):	
	apr_dir = '../model/'
	data_dir = '../corpus/'
	model_name = 'model_11.pt'
	epoch = 2
	bert_model = 'xlm-roberta-base'
	lr = 5e-5
	eps = 1e-8
	batch_size = 8
	training_data = 'train.txt'
	val_data = 'valid.txt'
	test_data = 'test.txt'
	test_out = 'test_prediction.csv'
	raw_prediction_output = 'raw_prediction.csv'
