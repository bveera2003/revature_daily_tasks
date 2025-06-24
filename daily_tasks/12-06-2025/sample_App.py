from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("SampleApp") \
    .master("local[*]") \
    .getOrCreate()

# Sample data
data = [("Alice", 25), ("Bob", 30), ("Cathy", 28)]
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Print schema
df.printSchema()

# Filter example
df.filter(df["Age"] > 27).show()

# Stop Spark session
spark.stop()
