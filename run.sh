export PATH_TO_FX=/media/samvid/Data/GitHub/openjfx-13.0.1_linux-x64_bin-sdk/javafx-sdk-13.0.1/lib
export MODULES=javafx.base,javafx.controls,javafx.fxml,javafx.graphics,javafx.media,javafx.swing,javafx.web
javac --module-path $PATH_TO_FX --add-modules $MODULES SlideShow.java
java --module-path $PATH_TO_FX --add-modules $MODULES SlideShow $1
