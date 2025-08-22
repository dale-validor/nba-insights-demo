import os
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('nba_stats_sample.csv')

# Ensure charts directory exists
os.makedirs('charts', exist_ok=True)

# 1) Top Scorers Bar Chart
df_sorted = df.sort_values('points', ascending=False).head(10)
plt.figure()
plt.bar(df_sorted['player'], df_sorted['points'])
plt.title('Top Scorers (PPG)')
plt.ylabel('Points per Game')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('charts/top_scorers.png')
plt.close()

# 2) Usage vs True Shooting Scatter
plt.figure()
plt.scatter(df['usg_pct'], df['ts_pct'])
for _, r in df.iterrows():
    plt.annotate(r['player'].split()[0], (r['usg_pct'], r['ts_pct']), fontsize=8, xytext=(3,3), textcoords='offset points')
plt.title('Usage vs True Shooting')
plt.xlabel('Usage Rate (USG%)')
plt.ylabel('True Shooting Percentage')
plt.tight_layout()
plt.savefig('charts/usage_vs_ts.png')
plt.close()

print('Charts generated in ./charts')