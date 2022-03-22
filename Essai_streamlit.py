# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:09:47 2022

@author: Anna
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("Sommaire")
pages = ["Dataviz","Feature Engineering","Modélisation",
         "Gains selon méthodes de pari", "Interprétation des modèles"]
page = st.sidebar.radio("Aller vers", pages)

if page == pages[0]:
    st.title("Data Visualisation")
    df = pd.read_csv("C:/Users/DARIDOR/Documents/Datascientest/Projet/df_model.csv")
    if st.checkbox('Voir le dataframe'):
        st.markdown("Dataframe de base (sans valeurs manquantes et avec colonnes renommées)")
        st.write(df)
    
elif page == pages[1]:        
    st.title("Feature Engineering")
    
    
elif page == pages[2]:
    st.title("Modélisation")  
    
    
    
elif page == pages[3]: 
    st.title("Gains selon méthodes de pari")


elif page == pages[4]:
    st.title("Interprétation des modèles")