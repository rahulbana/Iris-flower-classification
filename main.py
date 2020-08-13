import numpy as np
import pickle

def load_dependency():
	model_filename = "./models/model.pkl"  
	label_enc_filename = "./models/label_encoder.obj"
	scaler_filename = "./models/scaler.obj"
	
	with open(model_filename, 'rb') as file_model:  
	    model = pickle.load(file_model)


	with open(label_enc_filename, 'rb') as file_enc:  
	    lblencoder = pickle.load(file_enc)

	    
	with open(scaler_filename, 'rb') as file_scaler:  
	    scaler = pickle.load(file_scaler)

	return model, lblencoder, scaler


def predict_type(data, scaler, lblencoder, model):
	Xs = scaler.transform(np.array([data]))
	rs = model.predict(Xs)

	return lblencoder.inverse_transform(rs)[0]


