import streamlit as st
import pandas as pd
import pickle

from preprocessing_utils import *

st.write(""" 
    # Cluster News Articles
""")

articles = pd.read_csv('News_Articles_Mining-Clustering/clustered_articles.csv')

# Get selected category
selected_category = st.selectbox("Select a category:", ['politics', 'business', 'culture', 'sports'])

st.write('Selected Category:', selected_category)

k_means = pickle.load(open('News_Articles_Mining-Clustering/kmeans_model.pkl', 'rb'))

# Filter articles by selected category
clustered_articles = articles[articles['category'] == selected_category]

# Display clusters and URLs of related stories
for cluster in clustered_articles['clusters'].unique():
    st.write('Cluster:', cluster)
    cluster_articles = clustered_articles[clustered_articles['clusters'] == cluster]
    st.write('Related Articles:')
    st.write(cluster_articles[['article', 'url']])
    st.write('---')
