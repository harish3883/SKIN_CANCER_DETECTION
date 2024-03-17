import javax.media.jai.*;
import java.awt.image.renderable.ParameterBlockJAI;
import java.io.File;
import java.io.IOException;

public class ImageBackgroundRemoval {

    public static void main(String[] args) {
        try {
            // Specify the path to your input image
            String inputImagePath = "D:/Desktop/download.jpg";
            // Specify the path for saving the output image
            String outputImagePath = "D:/Desktop/download2.jpg";

            // Read the image file
            RenderedOp image = JAI.create("fileload", inputImagePath);

            // Create a ParameterBlockJAI to perform image operation
            ParameterBlockJAI pb = new ParameterBlockJAI("RemoveBackground");
            pb.addSource(image);

            // Create a new image with the background removed
            RenderedOp result = JAI.create("removeBackground", pb);

            // Save the result to the output image file
            File outputFile = new File(outputImagePath);
            JAI.create("filestore", result, outputFile.toString(), "JPEG");

            System.out.println("Background removed successfully!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
