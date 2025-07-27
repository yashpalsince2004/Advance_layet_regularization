import tenserflow as tf
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=3)
# history = model.fit(x_train, y_train,
#                     validation_data=(x_val, y_val),
#                     epochs=50,
#                     callbacks=[early_stop])
