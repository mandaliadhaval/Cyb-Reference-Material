import re
import tensorflow
regex_pattern = "#[\w]*"

noise_list = ["is", "a", "this", "an", "was", "were", "that"]
def _remove_noise(input_text):
    input_text=input_text.lower()
    print("Inside _remove_noise\n\n")
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list]
    noise_free_text = " ".join(noise_free_words)
    print(noise_free_text)

    return noise_free_text


def _remove_regex(input_text, regex_pattern):
    print("\n\nInside _regex_remove\n\n")
    urls = re.finditer(regex_pattern, input_text)
    for i in urls:
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text




noiseless_text=_remove_noise("Pegion is a bird. #nature")
reg_text=_remove_regex(noiseless_text,regex_pattern)
print(reg_text)




