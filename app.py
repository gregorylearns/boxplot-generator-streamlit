# import base64
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#         background-size: 50
#     }}
#     </style>
#     """,
#         unsafe_allow_html=True,
#     )


# add_bg_from_local("bg.jpg")


st.title("Boxplot Generator")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    plot_title = st.text_input("Plot Title:")

    number_input = st.text_area("Enter numbers (comma-separated):")

    max_value = st.number_input("Maximum Value:", value=100.0)
    min_value = st.number_input("Minimum Value:", value=60.0)
    bar_value = st.number_input("Bar Value:", value=75.0)

numbers_str = [s for s in number_input.replace("\n", ",").split(",") if s]
numbers = []
for number_str in numbers_str:
    try:
        number = float(number_str.strip())
        numbers.append(number)
    except ValueError:
        st.error(f"Invalid input: {number_str.strip()} is not a number.")
        numbers = []
        break

if numbers:
    fig, ax = plt.subplots(figsize=(3, 5))  # w x h Adjust width (6) as needed
    ax.boxplot(numbers)
    ax.axhline(bar_value, color="green")  #
    ax.set_ylim(min_value, max_value)
    ax.set_title(plot_title)
    current_yticks = ax.get_yticks()
    new_yticks = np.append(current_yticks, 75)
    ax.set_yticks(new_yticks)
    ax.set_xlim(left=0.85, right=1.5)
    # plt.style.use("seaborn-v0_8-pastel")
    plt.style.use("default")

    mean = np.mean(numbers)
    lowest = np.min(numbers)
    highest = np.max(numbers)
    count = len(numbers)
    stdev = np.std(numbers)
    q1 = np.quantile(numbers, 0.25)
    median = np.median(numbers)
    q3 = np.quantile(numbers, 0.75)

    textstr = "\n".join(
        (
            f"Mean: {mean:.2f}",
            f"Lowest: {lowest:.1f}",
            f"Highest: {highest:.1f}",
            f"\nCount: {count}",
            f"Stdev: {stdev:.2f}",
            f"Q1: {q1:.2f}",
            f"Median: {median:.2f}",
            f"Q3: {q3:.2f}",
        )
    )

    # These are matplotlib.rcParams default values
    props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

    # Place a text box in upper left in axes coords
    ax.text(
        0.45,
        0.95,
        textstr,
        transform=ax.transAxes,
        fontsize=10,
        horizontalalignment="left",
        verticalalignment="top",
        bbox=props,
    )
    with col2:
        st.pyplot(fig)
        # graph_created = True
# else:
#     graph_created = False

# if graph_created:
#     st.success("✓ Graph Created")
# else:
#     st.error("✗ Graph Not Created")

st.write("---")
st.write("*made with <3 for batch dextera & syncytium*")
