# Image Generator for ML

This repository extends the capabilities of Facebook Research's code related to the [CLEVR dataset](http://cs.stanford.edu/people/jcjohns/clevr/). 

It provides: (Documentation coming soon)
* All capabilities of the [original Facebook Research CLEVR dataset generation code.](https://github.com/facebookresearch/clevr-dataset-gen)
  * Can be used to generate additional random images for the CLEVR benchmark.
* Complete control to create custom images:
  * Camera, lighting, and objects can all be set to any 3D location
  * Objects can be placed on one another
  * Easy interface to add additional Blender object types


You can use this code to render synthetic images and compositional questions for those images, like this:

<div align="center">
  <img src="images/example1080.png" width="800px">
</div>

**Q:** How many small spheres are there? <br>
**A:** 2

**Q:**  What number of cubes are small things or red metal objects? <br>
**A:**  2

**Q:** Does the metal sphere have the same color as the metal cylinder? <br>
**A:** Yes

**Q:** Are there more small cylinders than metal things? <br>
**A:** No

**Q:**  There is a cylinder that is on the right side of the large yellow object behind the blue ball; is there a shiny cube in front of it? <br>
**A:**  Yes

If you find this code useful in your research then please reference this repository:
```
@misc{ml-image-generation-github,
  author = {Sebastian Pilarski},
  title = {ML Image Generation},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/SebastianPilarski/ml-image-generator}}
}
```
If generating images related to CLEVR, please also cite the original work by Justin Johnson et al. and Facebook Research:
```
@inproceedings{johnson2017clevr,
  title={CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning},
  author={Johnson, Justin and Hariharan, Bharath and van der Maaten, Laurens
          and Fei-Fei, Li and Zitnick, C Lawrence and Girshick, Ross},
  booktitle={CVPR},
  year={2017}
}
```

All code was developed and tested on OpenSuse Leap 15.2.
