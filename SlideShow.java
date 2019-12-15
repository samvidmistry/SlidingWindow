import java.io.File;
import java.util.*;

import javafx.application.Application;
import javafx.geometry.Rectangle2D;
import javafx.stage.Stage;
import javafx.stage.Screen;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.scene.media.MediaView;
import javafx.scene.paint.Paint;

public class SlideShow extends Application {
	public void start(Stage primaryStage) throws Exception {
		final Parameters args = getParameters();
		final List<String> rawArgs = args.getRaw();
		if(rawArgs.size() == 0) {
			System.out.println("Please enter path of video as first command line argument.");
			return;
		}

		final String path = rawArgs.get(0);
		final Media media = new Media(new File(path).toURI().toString());
		final MediaPlayer mediaPlayer = new MediaPlayer(media);
		final MediaView mediaView = new MediaView(mediaPlayer);
		mediaPlayer.setAutoPlay(true);

		final Group root = new Group();
		root.getChildren().add(mediaView);
		Rectangle2D bounds = Screen.getPrimary().getVisualBounds();
		final Scene scene = new Scene(root, bounds.getWidth(), bounds.getHeight());
		System.out.println("Width is " + bounds.getWidth() + ", height is " + bounds.getHeight());
		mediaView.setFitWidth(bounds.getWidth());
		mediaView.setFitHeight(bounds.getHeight());
		scene.setFill(Paint.valueOf("white"));
		primaryStage.setScene(scene);
		primaryStage.setTitle("Playing Video");
		primaryStage.setFullScreen(true);
		primaryStage.show();
	}

	public static void main(String[] args){
		launch(args);
	}
}
