# Build from the MATLAB base image
FROM mathworks/matlab:r2021a

# Add the init.m and plc.slx files
COPY plc.slx /usr/local/src/plc.slx
COPY init.m /usr/local/src/init.m

# Install wget
RUN sudo apt-get update && sudo apt-get install -y wget

# Install mpm
RUN sudo wget -q https://www.mathworks.com/mpm/glnxa64/mpm && sudo chmod +x mpm 

# Install MATLAB Toolboxes
RUN sudo ./mpm install --release=R2021a --destination=/opt/matlab/R2021a/ --products Simulink Signal_Processing_Toolbox DSP_System_Toolbox

# Run matlab
#RUN matlab /usr/local/src/init.m

EXPOSE 10001/udp
EXPOSE 10002/udp
EXPOSE 10003/udp
EXPOSE 10004/udp
EXPOSE 10005/udp
EXPOSE 10006/udp

