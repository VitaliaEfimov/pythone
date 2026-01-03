from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Загрузка данных MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализация изображений (приведение значений пикселей к диапазону [0, 1])
train_images = train_images / 255.0
test_images = test_images / 255.0

# Преобразование меток классов в one-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Определение архитектуры нейронной сети
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Входной слой, преобразующий матрицу 28х28 в вектор
    Dense(128, activation='relu'),   # Полносвязный скрытый слой с активацией ReLU
    Dense(10, activation='softmax')  # Выходной слой с softmax для классификации на 10 классов
])

# Компилирование модели
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Кросс-энтропия для multiclass-классификации
              metrics=['accuracy'])

# Обучение модели
model.fit(train_images, train_labels, epochs=5, batch_size=32)

# Оценка точности модели на тестовых данных
loss, accuracy = model.evaluate(test_images, test_labels)
print("Accuracy:", accuracy * 100, "%")