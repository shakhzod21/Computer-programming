
import random

# words for check 
words = ['man', 'woman', 'rabbit', 'dolphin', 'lion']
non_words = ['vbfj', 'pcvx', 'iasd', 'href', 'fbit']

# experimen no
def experiment2(num_trials):
    # intitialization 
    correct_word_count = 0
    correct_non_word_count = 0

    #range and random 
    for _ in range(num_trials):
        is_word = random.choice([True, False])
        
        if is_word:
            string = random.choice(words)
        else:
            string = random.choice(non_words)
        
        # string 
        response = input(f"Is '{string}' a meaningful word? (yes/no): ")
        
        # Check if the participant's response matches the true classification
        if (is_word and response.lower() == 'yes') or (not is_word and response.lower() == 'no'):
            if is_word:
                correct_word_count += 1
            else:
                correct_non_word_count += 1
    
    # acurracy alghoritm 
    word_accuracy = correct_word_count / len(words)
    non_word_accuracy = correct_non_word_count / len(non_words)
    
    return word_accuracy, non_word_accuracy

num_trials = 10

word_accuracy, non_word_accuracy = experiment2(num_trials)

# results
print(f"Accuracy for meaningful words: {word_accuracy * 100}%")
print(f"Accuracy for non-words: {non_word_accuracy * 100}%")
