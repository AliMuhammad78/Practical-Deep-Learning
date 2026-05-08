import tensorflow as tf
import time

print("\n" + "="*30)
print("TENSORFLOW GPU CHECK")
print("="*30)

# 1. Check TensorFlow Version
print(f"TF Version: {tf.__version__}")

# 2. Check for GPU
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    print(f"✅ Success! GPU Detected: {physical_devices}")
    
    # 3. Quick Matrix Multiplication Test (Optional but good)
    print("\nRunning a quick test on GPU...")
    with tf.device('/GPU:0'):
        a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
        c = tf.matmul(a, b)
        print("GPU Calculation Result:\n", c)
else:
    print("❌ GPU NOT FOUND.")
    print("Check if 'source ~/.bashrc' was run in this terminal.")

print("="*30 + "\n")