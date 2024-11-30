import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def clean_Yassine(df) :
    """
    clean the following variables : insee_%_const
                                    prelev_volume_obtention_mode_label_0 
                                    prelev_usage_label_2
    """

    #clean feature insee_%_const
    df['insee_%_const'] = pd.to_numeric(df['insee_%_const'], errors='coerce')
    df['insee_%_const'] = df['insee_%_const'].fillna(df['insee_%_const'].mean())

    #clean feature piezo_continuity_code
    df['piezo_continuity_code'] = df['piezo_continuity_code'].fillna(df['piezo_continuity_code'].mode()[0])

    #remove feature meteoname
    df = df.drop('meteoname', axis = 1)

    #remove feature hydro_method_label
    df = df.drop('hydro_method_label', axis = 1)

    #clean prelev_volume_obtention_mode_label_0
    df['prelev_volume_obtention_mode_label_0'] = df['prelev_volume_obtention_mode_label_0'].fillna(df['prelev_volume_obtention_mode_label_0'].mode()[0])

    #clean prelev_usage_label_2
    df['prelev_usage_label_2'] = df['prelev_usage_label_2'].fillna(df['prelev_usage_label_2'].mode()[0])
    


# Variables for label encoding
    label_encoding_features = [
        "prelev_volume_obtention_mode_label_0",
        'prelev_usage_label_2'
    ]

    label_encoders = {}
    for feature in label_encoding_features:
        encoder = LabelEncoder()
        df[feature] = encoder.fit_transform(dataset[feature])
        label_encoders[feature] = encoder  # Store encoders for inverse transformation if needed
    #dictionnary of encoders 
    encoder_dict = {'label_encoder' : encoder}
    encoded_features = { 'label_encoding_features' : [
        "prelev_volume_obtention_mode_label_0",
        'prelev_usage_label_2'
    ]}

    return df,encoder_dict, label_encoding_features



    
