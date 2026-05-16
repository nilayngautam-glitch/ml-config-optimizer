-- CREATE TABLE experiments (
-- 	id SERIAL PRIMARY KEY,
-- 	project_name VARCHAR(100) NOT NULL,
-- 	problem_type VARCHAR(100) NOT NULL,
-- 	dataset_size INT NOT NULL CHECK (dataset_size > 0),
-- 	backbone VARCHAR(100) NOT NULL,
-- 	activation VARCHAR(100) NOT NULL,
-- 	optimizer VARCHAR(100),
-- 	batch_size INT,
-- 	learning_rate FLOAT,
-- 	pretrained_weights VARCHAR(100),
-- 	augmentation VARCHAR(100),
-- 	val_accuracy FLOAT NOT NULL CHECK ( val_accuracy >= 0 AND val_accuracy <= 1),
-- 	val_loss FLOAT NOT NULL CHECK  (val_loss >= 0),
-- 	epochs INT NOT NULL CHECK (epochs > 0),
-- 	time_stamp TIMESTAMP DEFAULT NOW()
-- )


-- SELECT * FROM experiments;

-- INSERT INTO experiments (
--     project_name,
--     problem_type,
--     dataset_size,
--     backbone,
--     activation,
--     optimizer,
--     batch_size,
--     learning_rate,
--     pretrained_weights,
--     augmentation,
--     val_accuracy,
--     val_loss,
--     epochs
-- )
-- VALUES
-- ('Plant Disease Classifier', 'image_classification', 3500, 'ResNet50', 'ReLU', 'Adam', 32, 0.001, 'ImageNet', 'basic_flip_crop', 0.89, 0.34, 5),
-- ('Plant Disease Classifier', 'image_classification', 3500, 'EfficientNetB0', 'Swish', 'AdamW', 32, 0.0005, 'ImageNet', 'mixup', 0.92, 0.27, 5),
-- ('Plant Disease Classifier', 'image_classification', 3500, 'MobileNetV2', 'ReLU', 'Adam', 64, 0.001, 'ImageNet', 'basic_flip_crop', 0.87, 0.41, 5),

-- ('Skin Lesion Classifier', 'image_classification', 2200, 'ResNet50', 'ReLU', 'AdamW', 16, 0.0003, 'ImageNet', 'color_jitter', 0.84, 0.48, 5),
-- ('Skin Lesion Classifier', 'image_classification', 2200, 'EfficientNetB1', 'Swish', 'AdamW', 16, 0.0003, 'ImageNet', 'mixup', 0.86, 0.44, 5),

-- ('Animal Species Classifier', 'image_classification', 8500, 'ResNet101', 'ReLU', 'SGD', 32, 0.01, 'ImageNet', 'cutmix', 0.91, 0.31, 5),
-- ('Animal Species Classifier', 'image_classification', 8500, 'EfficientNetB2', 'Swish', 'AdamW', 32, 0.0005, 'ImageNet', 'randaugment', 0.94, 0.22, 5),
-- ('Animal Species Classifier', 'image_classification', 8500, 'MobileNetV3', 'HardSwish', 'Adam', 64, 0.001, 'ImageNet', 'basic_flip_crop', 0.90, 0.36, 5),

-- ('Road Sign Classifier', 'image_classification', 12000, 'ResNet50', 'ReLU', 'Adam', 32, 0.001, 'ImageNet', 'basic_flip_crop', 0.93, 0.24, 5),
-- ('Road Sign Classifier', 'image_classification', 12000, 'EfficientNetB0', 'Swish', 'AdamW', 32, 0.0005, 'ImageNet', 'randaugment', 0.95, 0.19, 5),

-- ('Mars Terrain Segmentation', 'segmentation', 16000, 'U-Net', 'ReLU', 'Adam', 16, 0.001, 'None', 'basic_flip_crop', 0.88, 0.39, 5),
-- ('Mars Terrain Segmentation', 'segmentation', 16000, 'ResNet50-U-Net', 'ReLU', 'AdamW', 16, 0.0003, 'ImageNet', 'basic_flip_crop', 0.91, 0.31, 5),
-- ('Mars Terrain Segmentation', 'segmentation', 16000, 'EfficientNet-U-Net', 'Swish', 'AdamW', 16, 0.0003, 'ImageNet', 'color_jitter', 0.90, 0.34, 5),

-- ('Medical Cell Segmentation', 'segmentation', 5000, 'U-Net', 'ReLU', 'Adam', 8, 0.001, 'None', 'basic_flip_crop', 0.82, 0.52, 5),
-- ('Medical Cell Segmentation', 'segmentation', 5000, 'ResNet34-U-Net', 'ReLU', 'AdamW', 8, 0.0003, 'ImageNet', 'elastic_transform', 0.86, 0.45, 5),

-- ('Crop Disease Detection', 'object_detection', 7000, 'YOLOv8n', 'SiLU', 'SGD', 16, 0.01, 'COCO', 'mosaic', 0.78, 0.61, 5),
-- ('Crop Disease Detection', 'object_detection', 7000, 'YOLOv8s', 'SiLU', 'AdamW', 16, 0.001, 'COCO', 'mosaic_mixup', 0.82, 0.55, 5),

-- ('Blood Demand Prediction', 'tabular_classification', 10000, 'MLP', 'ReLU', 'Adam', 64, 0.001, 'None', 'none', 0.81, 0.49, 5),
-- ('Blood Demand Prediction', 'tabular_classification', 10000, 'MLP', 'GELU', 'AdamW', 64, 0.0005, 'None', 'none', 0.83, 0.45, 5),

-- ('Customer Churn Prediction', 'tabular_classification', 25000, 'MLP', 'ReLU', 'Adam', 128, 0.001, 'None', 'none', 0.86, 0.38, 5),
-- ('Customer Churn Prediction', 'tabular_classification', 25000, 'MLP', 'GELU', 'AdamW', 128, 0.0005, 'None', 'none', 0.88, 0.34, 5),

-- ('Satellite Land Classifier', 'image_classification', 6000, 'ResNet50', 'ReLU', 'Adam', 32, 0.001, 'ImageNet', 'color_jitter', 0.88, 0.37, 5),
-- ('Satellite Land Classifier', 'image_classification', 6000, 'EfficientNetB1', 'Swish', 'AdamW', 32, 0.0005, 'ImageNet', 'randaugment', 0.91, 0.29, 5),
-- ('Satellite Land Classifier', 'image_classification', 6000, 'ConvNeXtTiny', 'GELU', 'AdamW', 32, 0.0003, 'ImageNet', 'randaugment', 0.93, 0.25, 5),

-- ('Waste Classification', 'image_classification', 4200, 'MobileNetV2', 'ReLU', 'Adam', 64, 0.001, 'ImageNet', 'basic_flip_crop', 0.85, 0.43, 5),
-- ('Waste Classification', 'image_classification', 4200, 'EfficientNetB0', 'Swish', 'AdamW', 32, 0.0005, 'ImageNet', 'mixup', 0.89, 0.35, 5);


-- SELECT * FROM experiments
-- WHERE problem_type = 'image_classification' 
-- AND dataset_size BETWEEN 3000 AND 10000
-- ORDER BY val_accuracy DESC, val_loss ASC
-- LIMIT 5;

-- ALTER TABLE experiment
-- ADD COLUMN iou FLOAT,
-- ADD COLUMN f1_score FLOAT,
-- ADD COLUMN mean_avg_precision FLOAT,
-- ADD COLUMN auc_roc FLOAT,
-- ADD COLUMN primary_metric VARCHAR(50) NOT NULL DEFAULT 'val_accuracy';

-- SELECT * FROM experiment


-- ALTER TABLE experiment
-- ADD COLUMN dataset_name VARCHAR(50) NOT NULL DEFAULT 'unknown',
-- ADD COLUMN seed INT,
-- ADD COLUMN freeze_strategy VARCHAR(100);

-- ALTER TABLE experiment
-- ADD COLUMN dropout VARCHAR(50),
-- ADD COLUMN regularization VARCHAR(50),
-- ADD COLUMN batch_normalization BOOLEAN;

--ALTER TABLE experiment
--ADD COLUMN loss_function VARCHAR(50)
