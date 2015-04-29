

# Source #

Dependencies: cmake build-essential opencc mercurial

To install the dependencies, you can run:
```
sudo apt-get install cmake build-essential opencc mercurial ibus
```

## libgooglepinyin ##

The library.

To compile and install the googlepinyin library, you can run:
```
hg clone http://code.google.com/p/libgooglepinyin/

cd libgooglepinyin

mkdir build; cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr

make
sudo make install
```


## ibus-googlepinyin ##

The ibus wrapper

To compile and install ibus-googlepinyin, you can run:
```
hg clone http://code.google.com/p/libgooglepinyin.ibus-wrapper/ ibus-googlepinyin

cd ibus-googlepinyin

mkdir build; cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr

make
sudo make install
```


---


## fcitx-googlepinyin ##

The fcitx wrapper

To compile and install fcitx-googlepinyin, you can run:
```
hg clone http://code.google.com/p/fcitx.fcitx-googlepinyin/ fcitx-googlepinyin

cd fcitx-googlepinyin

mkdir build; cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr

make
sudo make install
```


---


# Packages #

## Arch Linux ##

Packages is available in AUR.

## Ubuntu Linux ##

coming soon

## Debian Linux ##

coming soon

## Fedora Core ##

coming soon