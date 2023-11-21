inputDir = getDirectory("Choose input directory");
outputDir = getDirectory("Choose output directory");

list = getFileList(inputDir);
for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".txt")) {
        run("Text Image... ", list[i]);
		saveAs("Jpeg", outputDir + list[i]);
		close("*");
    }
}