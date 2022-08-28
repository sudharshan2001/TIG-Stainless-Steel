import tensorflow as tf

data_augmentation = tf.keras.Sequential([
  tf.keras.layers.RandomFlip('horizontal'),
  tf.keras.layers.RandomRotation(0.2),
])

effnet_b7 = tf.keras.applications.efficientnet.EfficientNetB7(
    include_top=False,
    input_shape=(128,128,3),
    pooling="max",

)
def get_model():
	inputs = tf.keras.Input(shape=(128, 128, 3))
	x = data_augmentation(inputs)
	x = resnet_layers(x)

	x = tf.keras.layers.Flatten()(x)
	x = tf.keras.layers.Dense(256, activation='relu')(x)
	x = tf.keras.layers.Dropout(0.2)(x)
	outputs = tf.keras.layers.Dense(6, activation = 'softmax')(x)

	model = tf.keras.Model(inputs, outputs)
	return model
