def fetch_stats(selected_user, df):
    if selected_user == 'Overall':
        #1. fetch number of messages
        num_messages = df.shape[0]
        #2. fetch number of words
        words = []
        for message in df['message']:
            words.extend(message.split())
        return num_messages,words
    else:
        new_df = df[df['user'] == selected_user]
        words=[]
        for message in new_df['message']:
            words.extend(message.split())
        return num_messages, words