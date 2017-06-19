+ Download the latest version of WEKA on your Linux machines from here: http://www.cs.waikato.ac.nz/ml/weka/downloading.html.
+ Extract the .zip file in your home directory (echo $HOME), eg. mine is '/home/cla315/weka-3-8-1'
+ Follow instrucion from the following links:
    + https://weka.wikispaces.com/Databases
    + https://weka.wikispaces.com/CLASSPATH

## Step 1: Download JDBC Driver from https://dev.mysql.com/downloads/connector/j/
In my case, my mysql-connector-java-5.1.42-bin.jar is located in the following directory: /home/cla315/jars/
Now, open a shell and execute the following command:

    bash
    export CLASSPATH=$CLASSPATH:/home/cla315/jars/mysql-connector-java-5.1.42-bin.jar
    (to check if it worked, echo $CLASSPATH)
+ Looks like you also have to save the JDBC Driver file in WEKA path, eg.:/home/cla315/weka-3-8-1/mysql-connector-java-5.1.42-bin.jar
  
## Step 2: Get this properties file from the weka.jar (extract the .jar file anywhere but current folder). 
+ You'll find the properties file for MySql database in the sub-folder, 
ie. /weka/experiment/DatabaseUtils.props.mysql
+ Copy this props file to home directory can change its name to DatabaseUtils.props 
eg. /home/cla315/DatabaseUtils.props
because Weka only looks for the DatabaseUtils.props file.
+ Next, modify the following content in the props file:
    
      #JDBC driver (comma-separated list)
      jdbcDriver=com.mysql.jdbc.Driver (or org.gjt.mm.mysql.Driver)
      #database URL
      jdbcURL=jdbc:mysql://server.my.domain:3306/MyDatabase
      (eg. jdbcURL=jdbc:mysql://cs-oschulte-01.cs.sfu.ca:3306/chao_draft)

## Step 3: Run the following start script for Weka Explorer:

    #! /bin/bash
    # Path to weka
    WEKA_PATH=~/weka-3-8-1/
    # add mysql-connector (manually copied to weka path) and weka to classpath
    CP="$CLASSPATH:/usr/share/java/:$WEKA_PATH/mysql-connector-java-5.1.42-bin.jar:$WEKA_PATH/weka.jar"
    # use the connector of debian package libmysql-java
    # CP="$CLASSPATH:/usr/share/java/:$WEKA_PATH/weka.jar"
    echo "used CLASSPATH: $CP"
    # start Explorer
    java -cp $CP -Xmx500m weka.gui.explorer.Explorer
+ You can save the above script as eg.'script_weka.sh', and run it with the command "bash script_weka.sh" everytime you need to start Weka Explorer.
    

## Trouble shooting:
   + Sometimes (e.g. with MySQL) it can happen that a column type cannot be interpreted. In that case it is necessary to map the name of the column type to the Java type it should be interpreted as.
    For different column types in MySQL, refer to: http://weka.8497.n7.nabble.com/No-suitable-driver-td13364.html
      eg.If the following error occurs: "Couldn't read from database: Unkown data type: INT. Add entry in weka/experiment..."
         Modify the props file by simply adding one line: INT = 5
