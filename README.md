# CS421-project1 (eye tracker correction algorithms)

**To look at my code go to the branch called project-1**

In this project I started by using a dataset created by the professor where it simulates result from a calibrated eye tracker, and developed 5 different type or error (noise, downward slope, downward shift, within the line error, between the line error. After that I used the 10 algorithms mentioned in the paper Carr, Jon W., et al. "Algorithms for the automated correction of vertical drift in eye-tracking data." Behavior Research Methods 54.1 (2022): 287-310. These methods are attach, chain, regress, warp, cluster, compare, merge, segment, split, stretch.

After having all the algorithms working, I used the Jupyter notebook (the second notebook) to test the accuracy of all correction algorithms with all 5 different errors. After running all each error y created a graph where you can observe the how well the algorithm performs compared to each other. As an extension of the project, I tested the algorithms with real data.

