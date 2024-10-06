Hi! Yana and Dea here!

## Machine Learning model

Here we put the code that we used to train our model, and to detect quakes on the test data

**Main files**
- **cnn+lstm_v1.ipynb** is the first version of our model. We implemented the architecture using Convolutional Neural Network layers along with the layers of Long Short-Term Memory Network. This combination allowed the neural network to focus both on the local patterns, and on the temporal dependencies in bigger picture.
- **cnn+lstm_feature_engin_v2.ipynb** is the second version. We built up upon the v1, using the feature engineering. We added the second feature, which is the derivative of the velocity. It helped to provide the model with the data on how fast the velocity changes, which in turn will help to focus more on the spikes.

Folder **predictions_plots_v1** and **predictions_plots_v2** contains the visualised predictions for each of the test files. Additionally, the folder with combined figures was created, where you can compare them side by side

## Next steps
There are a lot of possible improvements that could be adde to the existing code to improve the accuracy. For example:
- Preliminary processing of the data to remove the noise
- Engineering of another feature using Fourier transform. It can provide the model with better insights in the data, rather than feeding just the raw velocities.
- Tuning the hyperparameters used for learning
- Tuning the parameters in the model's architecture (e.g layer size)
- Comparing performance of different models, and possibly combining them in two-steps detection
