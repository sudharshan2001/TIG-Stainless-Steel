def get_model(classes):
    
    #Input shape = [width, height, color channels]
    inputs = layers.Input(shape=(256, 256, 3))
    
    # Block One
    x = layers.Conv2D(filters=16, kernel_size=1, padding='valid')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.2)(x)

    # Block Two
    x = layers.Conv2D(filters=32, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.2)(x)
    
    # Block Three
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.4)(x)
    
    # Block four
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.4)(x)
    
    # Block five
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.4)(x)

    # Block six
    x = layers.Conv2D(filters=64, kernel_size=1, padding='valid')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPool2D()(x)
    x = layers.Dropout(0.4)(x)
    
    # Head

    x = layers.Flatten()(x)
    x = layers.Dense(512, activation='relu')(x)

    output = layers.Dense(classes, activation='softmax')(x)
    
    model = tf.keras.Model(inputs=[inputs], outputs=output)
    
    return model

model = get_model(6)
model.summary()
