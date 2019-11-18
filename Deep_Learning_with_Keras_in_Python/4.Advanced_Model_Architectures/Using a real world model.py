'''
Okay, so Ivy's picture is ready to be used by ResNet50. It is stored in img_ready and now looks like this:


ResNet50 is a model trained on the Imagenet dataset that is able to distinguish between 1000 different objects. ResNet50 is a deep model with 50 layers, you can check it in 3D here.

ResNet50 and decode_predictions have both been imported from keras.applications.resnet50 for you.

It's time to use this trained model to find out Ivy's breed!
'''


# Instantiate a ResNet50 model with imagenet weights
model = ResNet50(weights='imagenet')

# Predict with ResNet50 on your already processed img
preds = model.predict(img_ready)

# Decode predictions
print('Predicted:', decode_predictions(preds, top=3)[0])