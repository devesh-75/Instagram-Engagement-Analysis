from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Instagram Engagement Analysis") \
    .getOrCreate()

# Load dataset
df = spark.read.csv("data/dataset.csv", header=True, inferSchema=True)

# Show first 5 rows
df.show(5)

# Print schema
df.printSchema()


from pyspark.sql.functions import col, avg, count

# -------------------------------
# DATA CLEANING
# -------------------------------

print("Checking NULL values:")
df.select([count(col(c)).alias(c) for c in df.columns]).show()

# -------------------------------
# BASIC ANALYSIS
# -------------------------------

print("Average Engagement Metrics:")
df.select(
    avg("likes").alias("avg_likes"),
    avg("comments").alias("avg_comments"),
    avg("shares").alias("avg_shares")
).show()

# -------------------------------
# ENGAGEMENT BY POST TYPE
# -------------------------------

print("Engagement by Post Type:")
df.groupBy("post_type").agg(
    avg("likes").alias("avg_likes"),
    avg("comments").alias("avg_comments")
).show()

# -------------------------------
# BEST POSTING HOUR
# -------------------------------

print("Best Posting Hour (by avg likes):")
df.groupBy("posted_hour").agg(
    avg("likes").alias("avg_likes")
).orderBy(col("avg_likes").desc()).show()



# -------------------------------
# FEATURE ENGINEERING
# -------------------------------

print("Creating Engagement Score...")

df = df.withColumn(
    "engagement_score",
    (col("likes") + col("comments") + col("shares")) / col("followers")
)

# Show new column
df.select("likes", "comments", "shares", "followers", "engagement_score").show(5)

# -------------------------------
# HIGH vs LOW ENGAGEMENT COUNT
# -------------------------------

print("Engagement Label Distribution:")
df.groupBy("engagement_label").count().show()


# -------------------------------
# ML PREPARATION
# -------------------------------

from pyspark.ml.feature import StringIndexer, VectorAssembler

print("Preparing Data for Machine Learning...")

# Convert post_type (text) to numeric
indexer = StringIndexer(inputCol="post_type", outputCol="post_type_index")
df = indexer.fit(df).transform(df)

# Select features
features = [
    "followers",
    "likes",
    "comments",
    "shares",
    "views",
    "watch_time",
    "hashtags_count",
    "caption_length",
    "posted_hour",
    "post_type_index"
]

# Combine features into vector
assembler = VectorAssembler(inputCols=features, outputCol="features")
df = assembler.transform(df)

# Show final dataset for ML
df.select("features", "engagement_label").show(5)


# -------------------------------
# MACHINE LEARNING MODEL
# -------------------------------

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

print("Training Machine Learning Model...")

# Split data
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Train model
lr = LogisticRegression(
    featuresCol="features",
    labelCol="engagement_label"
)

model = lr.fit(train_data)

# Make predictions
predictions = model.transform(test_data)

# Show predictions
predictions.select("features", "engagement_label", "prediction").show(5)

# Evaluate model
evaluator = BinaryClassificationEvaluator(
    labelCol="engagement_label"
)

accuracy = evaluator.evaluate(predictions)

print("Model Accuracy:", accuracy)