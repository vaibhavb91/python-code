import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data.csv" 
df = pd.read_csv(file_path)

print("\n📄 First 5 Rows of the Data:")
print(df.head())


print("\n📊 Data Shape (rows, columns):", df.shape)
print("\n📋 Column Names:", df.columns.tolist())
print("\n🔍 Data Types:")
print(df.dtypes)

print("\n❓ Missing Values:")
print(df.isnull().sum())

# 4. Summary Statistics
print("\n📈 Summary Statistics:")
print(df.describe())

# 5. Clean Column Names (optional)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# 6. Drop missing values (optional)
df_cleaned = df.dropna()

# 7. Basic Analysis (if numeric column exists)
if not df_cleaned.select_dtypes(include="number").empty:
    print("\n🔢 Numeric Columns Summary:")
    for col in df_cleaned.select_dtypes(include="number").columns:
        print(f"\n📌 Column: {col}")
        print("  ➤ Mean   :", df_cleaned[col].mean())
        print("  ➤ Median :", df_cleaned[col].median())
        print("  ➤ Mode   :", df_cleaned[col].mode()[0])

# 8. Correlation Heatmap (for numeric columns)
if df_cleaned.select_dtypes(include="number").shape[1] >= 2:
    print("\n📊 Generating correlation heatmap...")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_cleaned.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()

# 9. Histogram of first numeric column
first_numeric = df_cleaned.select_dtypes(include="number").columns[0]
print(f"\n📊 Generating histogram for '{first_numeric}'...")
plt.figure(figsize=(8, 4))
sns.histplot(df_cleaned[first_numeric], kde=True, color="skyblue")
plt.title(f"{first_numeric.capitalize()} Distribution")
plt.xlabel(first_numeric)
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# # 10. Save cleaned data
# df_cleaned.to_csv("cleaned_data.csv", index=False)
# print("\n✅ Cleaned data saved to 'cleaned_data.csv'")