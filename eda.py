import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week",
    "native_country", "income"
]

def load_data(train_path="adult.data", test_path="adult.test"):
    train_df = pd.read_csv(
        train_path,
        header=None,
        names=COLUMNS,
        skipinitialspace=True,
        na_values="?"
    )

    test_df = pd.read_csv(
        test_path,
        header=None,
        names=COLUMNS,
        skiprows=1,
        skipinitialspace=True,
        na_values="?"
    )

    test_df["income"] = test_df["income"].str.replace(".", "", regex=False)

    return pd.concat([train_df, test_df], ignore_index=True)

def detect_missing_values(df):
    print("\nMissing values per column:")
    print(df.isnull().sum())

def quantify_missing_data(df):
    missing_count = df.isnull().sum()
    missing_percent = (df.isnull().mean() * 100).round(2)

    missing_df = pd.DataFrame({
        "missing_count": missing_count,
        "missing_percent": missing_percent
    }).sort_values(by="missing_count", ascending=False)

    print("\nMissing data summary:")
    print(missing_df)

    return missing_df

def drop_missing_data(df):
    return df.dropna()

def create_plots(df):
    df["income"].value_counts().plot(kind="bar", title="Income Distribution")
    plt.tight_layout()
    plt.savefig("income_distribution.png")
    plt.close()

    df["age"].plot(kind="hist", bins=20, title="Age Distribution")
    plt.tight_layout()
    plt.savefig("age_distribution.png")
    plt.close()

    df["hours_per_week"].plot(kind="hist", bins=20, title="Hours per Week Distribution")
    plt.tight_layout()
    plt.savefig("hours_per_week_distribution.png")
    plt.close()

    print("\nPlots saved successfully.")

def main():
    df = load_data("adult.data", "adult.test")

    print("=== BEFORE CLEANING ===")
    print("Rows before cleaning:", len(df))
    detect_missing_values(df)
    quantify_missing_data(df)

    cleaned_df = drop_missing_data(df)

    print("\n=== AFTER CLEANING ===")
    print("Rows after cleaning:", len(cleaned_df))
    detect_missing_values(cleaned_df)
    quantify_missing_data(cleaned_df)

    create_plots(cleaned_df)

if __name__ == "__main__":
    main()