import pandas as pd
import numpy as np
import fs

def filter(filter,dataset):
	df = pd.read_csv(dataset)
	data = fs.bootstrap(df)
	if filter == "relieF":
		R = fs.relieF(data)
		return (fs.dispcolumns(df,R))

	elif filter == "fishers":
		R = fs.fishers(data)
		return (fs.dispcolumns(df,R))
	elif filter == "mim":
		R = fs.mim(data)
		return (fs.dispcolumns(df,R))
	elif filter == "icap":
		R = fs.icap(data)
		return (fs.dispcolumns(df,R))
	elif filter == "cmim":
		R = fs.cmim(data)
		return (fs.dispcolumns(df,R))
	elif filter == "jmi":
		R = fs.jmi(data)
		return (fs.dispcolumns(df,R))
	elif filter == "disr":
		R = fs.disr(data)
		return (fs.dispcolumns(df,R))
	else:
		return ("select the filter first")
