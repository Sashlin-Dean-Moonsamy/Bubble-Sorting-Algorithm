# Define bubble sort function
def bubble_sort(array):

    # Set value of i to the length of array - 1
    i = len(array) - 1

    # Create while loop to loop over each value
    while i != 0:

        # Create for loop for comparison
        for j in range(i):

            # Swap values if required
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

        # Subtract 1 from i after each for loop iteration
        i -= 1
