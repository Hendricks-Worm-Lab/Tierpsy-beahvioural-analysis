inputDir = getDirectory("Choose input directory");
outputDir = getDirectory("Choose output directory");

list = getFileList(inputDir);
for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".avi")) {
        open(inputDir + list[i]);
        // Add your ImageJ commands here
        run("Duplicate...", "duplicate");
        selectWindow(list[i]);
        close();
		run("Invert", "stack");
		imp1 = getTitle();
		run("Z Project...", "stop=2 projection=[Average Intensity]");
		imp2 = getTitle();
		imageCalculator("Subtract create stack",imp1,imp2);
		run("Invert", "stack");
        saveAs("AVI", outputDir + list[i]);
        close("*");
    }
}