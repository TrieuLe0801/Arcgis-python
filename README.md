# Arcgis-python
a Arcgis on python 

## Requirement
arcpy<br>
esri

- For Anaconda, install Ananaconda is a requirement:
  - For Ubuntu 18.04: Following this step to install [Anaconda](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart)
  - For Ubuntu 20.04: Following this step to install [Anaconda](https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/)
  - For MacOS: Following this step to install [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
  - Following this script to set up environment:<br>
  ```
  conda create --prefix = ./venv/ python=3.8.0
  conda activate venv/
  conda install --file requirements.txt -c esri 
  ```