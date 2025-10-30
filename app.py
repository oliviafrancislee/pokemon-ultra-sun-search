"""
Pokemon Ultra Sun Search Application
A simple Streamlit UI for searching and filtering Pokemon from Ultra Sun.
"""

import streamlit as st
import pandas as pd
from pokemon_data import get_pokemon_data as load_pokemon_data


@st.cache_data
def get_pokemon_data():
    """Load Pokemon data with caching."""
    return load_pokemon_data()


def main():
    st.set_page_config(
        page_title="Pokemon Ultra Sun Search",
        page_icon="⚡",
        layout="wide"
    )
    
    st.title("⚡ Pokemon Ultra Sun Search")
    st.markdown("Search and filter Pokemon from Pokemon Ultra Sun")
    
    # Load data
    with st.spinner("Loading Pokemon data..."):
        df = get_pokemon_data()
    
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Type filter
    all_types = set()
    for _, row in df.iterrows():
        if pd.notna(row['type1']):
            all_types.add(row['type1'])
        if pd.notna(row['type2']):
            all_types.add(row['type2'])
    
    type_filter = st.sidebar.multiselect(
        "Filter by Type",
        options=sorted(all_types),
        default=[]
    )
    
    # Final evolution filter
    final_evolution_only = st.sidebar.checkbox(
        "Show Final Evolutions Only",
        value=False
    )
    
    # Sort options
    st.sidebar.header("Sorting")
    sort_order = st.sidebar.radio(
        "Sort by Total Stats",
        options=["None", "Ascending", "Descending"],
        index=0
    )
    
    # Apply filters
    filtered_df = df.copy()
    
    # Type filter
    if type_filter:
        filtered_df = filtered_df[
            filtered_df['type1'].isin(type_filter) | 
            filtered_df['type2'].isin(type_filter)
        ]
    
    # Final evolution filter
    if final_evolution_only:
        filtered_df = filtered_df[filtered_df['next_evolution'].isna()]
    
    # Apply sorting
    if sort_order == "Ascending":
        filtered_df = filtered_df.sort_values('total_stats', ascending=True)
    elif sort_order == "Descending":
        filtered_df = filtered_df.sort_values('total_stats', ascending=False)
    
    # Display summary
    st.subheader(f"Showing {len(filtered_df)} Pokemon")
    
    # Display data
    if len(filtered_df) > 0:
        # Format the dataframe for display
        display_df = filtered_df.copy()
        display_df['prev_evolution'] = display_df['prev_evolution'].fillna('-')
        display_df['next_evolution'] = display_df['next_evolution'].fillna('-')
        display_df['type2'] = display_df['type2'].fillna('-')
        
        # Reorder columns for better display
        column_order = [
            'name', 'type1', 'type2', 'prev_evolution', 'next_evolution',
            'total_stats', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed'
        ]
        display_df = display_df[column_order]
        
        # Rename columns for display
        display_df.columns = [
            'Name', 'Type 1', 'Type 2', 'Previous Evolution', 'Next Evolution',
            'Total Stats', 'HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed'
        ]
        
        # Display as a table
        st.dataframe(
            display_df,
            use_container_width=True,
            height=600,
            hide_index=True
        )
        
        # Show statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Pokemon", len(filtered_df))
        
        with col2:
            st.metric("Avg Total Stats", f"{filtered_df['total_stats'].mean():.1f}")
        
        with col3:
            st.metric("Highest Stats", filtered_df['total_stats'].max())
        
        with col4:
            st.metric("Lowest Stats", filtered_df['total_stats'].min())
        
        # Top 5 by stats
        if len(filtered_df) >= 5:
            st.subheader("Top 5 by Total Stats")
            top5 = filtered_df.nlargest(5, 'total_stats')[['name', 'type1', 'type2', 'total_stats']]
            top5.columns = ['Name', 'Type 1', 'Type 2', 'Total Stats']
            st.table(top5.reset_index(drop=True))
    else:
        st.warning("No Pokemon match the selected filters.")
    
    # Instructions
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### How to Use
    - **Type Filter**: Select one or more types to filter Pokemon
    - **Final Evolutions**: Check to show only Pokemon that don't evolve further
    - **Sorting**: Choose to sort by total base stats
    """)


if __name__ == "__main__":
    main()
