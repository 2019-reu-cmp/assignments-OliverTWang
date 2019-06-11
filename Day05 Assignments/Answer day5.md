1: nd.array() have stores data of same type and size. The type and elements are all fixed. It can be called more conveniently, can use a few integers of Ntuple in shape() to store a higher dimension matrix, whilst lists are only 1-dimensional. It also calculates faster.

2: When changing the array you change all the elements in the array at once, but it won't be stored unless deifned as another new array e.g.

3: functions like .mean() or .std() computes the correspondingstatistic value of all single elements in the numpy array, but we can also specify it by having functions like .std(axis=1) that only calculates the standard deviation of the second axis

4: see other attachments
