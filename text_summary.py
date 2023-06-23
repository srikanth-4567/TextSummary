import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    tokens = [token.text for token in doc]
    word_freq = {}
    
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    
    max_freq = max(word_freq.values())
    
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq
    
    sent_tokens = [sent for sent in doc.sents]
    sent_scores = {}
    
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    
    select_len = int(len(sent_tokens) * 0.3)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    
    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))

# Call the function with the input text
text=""" Global Recession 2023: According to the Centre for Economics and Business Research (CEBR), a global recession will start in 2023. A global recession is predicted by other agencies as well to begin in 2023. New borrowing costs put in place to fight inflation cause several economies to shrink. According to the British consultancy’s annual World Economic League Table, the global economy topped $100 trillion for the first time in 2022 but will halt in 2023 as governments continue to struggle against growing costs.

Buy Prime Test Series for all Banking, SSC, Insurance & other exams

Global Recession 2023: CEBR Prediction
The researcher’s findings are more negative than the most recent IMF forecast. According to Bloomberg, this organisation warned in October that more than a third of the world’s economies will collapse and that there is a 25% possibility that in 2023, global GDP will expand by less than 2%, which it characterizes as a worldwide recession.

The global gross domestic product will have doubled by 2037 as developing economies catch up to the wealthier ones. According to Bloomberg, the East Asia and Pacific region will produce more than a third of the world’s output by 2037, while Europe’s share will drop to less than a fifth as a result of changing power dynamics.

The data from the IMF’s World Economic Outlook and an internal model serve as the foundation for the Centre for Economics and Business Research’s estimates of growth, inflation, and currency rates.

Global Recession 2023 Impact on India
The report predicts that India’s economy will reach $10 trillion by 2035 and rank third globally by 2032.
Since the US is one of the great superpowers, a mild or deeper recession will eventually have worldwide repercussions.
The crisis ultimately grew and spread into a global economic shock, manifesting itself in a number of European bank failures, drops in several stock indices, and significant falls in the value of the Indian market.
Given that Indian businesses had significant outsourcing agreements with US clients, a slowdown in the US economy was undoubtedly terrible news for India.
Over the years, India’s exports to the US have grown. However, India was impacted and managed to survive the severe financial crisis of September 2008.
Global Recession 2008
Before 2008, the Great Recession had already started. The first warning indicators appeared in 2006 when home values started to decline. By August 2007, the Federal Reserve had injected $24 billion in additional liquidity into the banking system in response to the subprime mortgage crisis. By October 2008, Congress had authorized the Troubled Asset Relief Program, a $700 billion bank bailout. Obama proposed the $787 billion economic stimulus programme in February 2009, helping to prevent a global depression.

Factors that Saved India from Global Recession 2008
The Indian economy was shielded from the negative effects of the global recession by a number of factors.
Due to the fact that India’s economy is heavily dependent on agriculture, it was prevented from experiencing mass unemployment like other impacted nations.
The mortgage-backed securities and credit that turned toxic and brought down western financial institutions were nearly entirely ignored by Indian banks and financial institutions at the time.
Despite the fact that the Great Recession had a significant negative impact on India’s merchandise exports, IT and BPO exports did not suffer as a result.
Despite the financial crisis, foreign direct investment increased.
Financiers stopped flowing into India, but long-term owners of companies and plants continued with their ongoing projects."""
summary, doc, len_raw, len_summary = summarizer(text)
#print("Summary:", summary)
#print("Length of original text:", len_raw)
#print("Length of summary text:", len_summary)
