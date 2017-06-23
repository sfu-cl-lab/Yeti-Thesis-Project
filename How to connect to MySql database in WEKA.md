+ Download the latest version of WEKA on your Linux/MAC OS machine from here: http://www.cs.waikato.ac.nz/ml/weka/downloading.html.
+ Extract the .zip file in your home directory (echo $HOME), e.g. mine is '/home/cla315/weka-3-8-1'
+ The following step-by-step instrucions are summarized from the two links below:
    + https://weka.wikispaces.com/Databases
    + https://weka.wikispaces.com/CLASSPATH


## Step 1: Set up JDBC Driver
+ Download JDBC Driver from here: https://dev.mysql.com/downloads/connector/j/
+ Save the mysql-connector-java-5.1.42-bin.jar file in a fold, e.g./home/cla315/jars/
+ Now, open a shell and execute the following command:

        bash
        export CLASSPATH=$CLASSPATH:/home/cla315/jars/mysql-connector-java-5.1.42-bin.jar
        (to check if it worked, echo $CLASSPATH)
  
## Step 2: Modify the property file for the database you are using
+ Get the properties file from the weka.jar or weka-src.jar jar-archive, both part of a normal Weka release. 
+ If you open up one of those files, you'll find the properties file in the sub-folder weka/experiment. e.g. /weka/experiment/DatabaseUtils.props.mysql
+ You have to delete the extraced sub-folder named "weka", otherwise you couldn't open the explorer from terminal!
+ Copy this props file to your home directory and change its name to DatabaseUtils.props 
e.g. /home/cla315/DatabaseUtils.props, because Weka only looks for the DatabaseUtils.props file.
+ Next, modify the following content in the DatabaseUtils.props file:
    
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
+ On a Linux system you can save the above script, e.g. as a 'script_weka.sh' file, and run it in terminal "bash script_weka.sh" everytime you need to start Weka Explorer
+ But on a MAC OS system, changing the JAVA CLASSPATH permanently is tricky. It's easier to just run the above script line by line in terminal. 

## Trouble Shooting for the "Unknow data type" Error:
   + Sometimes (e.g. with MySQL) it can happen that a column type cannot be interpreted. In that case it is necessary to map the name of the column type to the Java type it should be interpreted as.
   + For different column types in MySQL, refer to: http://weka.8497.n7.nabble.com/No-suitable-driver-td13364.html
    + e.g.If the following error occurs: "Couldn't read from database: Unkown data type: INT. Add entry in weka/experiment..."
    + Modify the props file by simply adding one line: INT = 5
