#!/usr/bin/env sh

PROGNAME=$0;

##
## Адресс
##

IP="127.0.0.1"

PORT="9000"

ADDRESS="${IP}:${PORT}"


##
## Узел
##

HTTP_WORKERS="10"

PROCESSES="10"

XUID="1000"

XGID="2000"

HARAKIRI="5000"

MAX_REQUESTS="5000"

##
##
##

NODE_NAME="grizzlyhockey"

NODE="${NODE_NAME}-${PORT}-${PROCESSES}-${HARAKIRI}-${MAX_REQUESTS}"


##
## Папка проекта
## PROJECT_DIR="${PWD}"
##
PROJECT_DIR=$(dirname "${PROGNAME}");


PROJECT_NAME="project"


##
## Папка статических объектов
##

STATIC_SUBDIR="project/media"

STATIC_DIR="${PROJECT_DIR}/${STATIC_SUBDIR}"

STATIC_URL="/media"

##
## Pid проекта
##
PID_DIR="/tmp"

PID_NAME="${NODE}.pid"

PID_FILE="${PID_DIR}/${PID_NAME}"

##
## Log проекта
##

LOG_DIR="/var/log/grizzlyhockey"

LOG_NAME="${NODE}.log"

LOG_FILE="${LOG_DIR}/${LOG_NAME}"

# --uid="${XUID}"                                             \
# --gid="${XGID}"                                             \


[[ x$0 = "x" ]] && PROGNAME="grizzlyhockey_start";

warn () {
    echo "WARN:${PROGNAME}: $@";
}

error () {
    echo "ERROR:${PROGNAME}: $@" ; exit 1 ;
}

notice() {
    [[ "x${VERBOSE}" = "xyes" ]] && echo "# $@" 1>&2;
}

noticeall() {
    notice "ADDRESS         =   ${ADDRESS}";
    notice "PROJECT_DIR     =   ${PROJECT_DIR}";
    notice "LOG_FILE        =   ${LOG_FILE}";
    notice "PROJECT_NAME    =   ${PROJECT_NAME}";
    notice "PID_FILE        =   ${PID_FILE}";
    notice "PROCESSES       =   ${PROCESSES}";
    notice "HARAKIRI        =   ${HARAKIRI}";
    notice "MAX_REQUESTS    =   ${MAX_REQUESTS}";
    notice "STATIC_URL      =   ${STATIC_URL}";
    notice "STATIC_DIR      =   ${STATIC_DIR}";
    notice ""
    notice "    MODE: ${MODE}";
    notice ""
}

usage () {
cat <<CPUSAGE
Grizzlyhockey node managment utility for changing it state.
$PROGNAME [-h]|[[-m]|[-M]|[-a] [-v]]

    -h | --help     shows this test.
    -s | --start    starts or restarts the node.
    -S | --stop     stops node.
    -r | --reload   reloads node.
    -v | --verbose  uses verbose mode. It tells about really actions.

CPUSAGE
}

show_usage(){
    usage;
    exit 0;
}

wrong_usage(){
    usage;
    error $'\n'"$@"$'\n';
}

##
## --------------------------------------------------------------------------
##

do_start () {
    mkdir -p "${LOG_DIR}"
    notice "uwsgi <PARAMS ... >"
    uwsgi                                                           \
        --plugins python                                            \
        --http="${ADDRESS}"                                         \
        --chdir="${PROJECT_DIR}"                                    \
        --daemonize="${LOG_FILE}"                                   \
        --module="${PROJECT_NAME}.wsgi:application"                 \
        --env "DJANGO_SETTINGS_MODULE=${PROJECT_NAME}.settings"     \
        --master                                                    \
        --pidfile="${PID_FILE}"                                     \
        --processes="${PROCESSES}"                                  \
        --harakiri="${HARAKIRI}"                                    \
        --max-requests="${MAX_REQUESTS}"                            \
        --static-map "${STATIC_URL}/=${STATIC_DIR}/"                \
        --vacuum
}

do_reload(){
    notice "uwsgi --reload ${PID_FILE}";
    uwsgi --reload "${PID_FILE}";
}


do_stop(){
    notice "uwsgi --stop ${PID_FILE}";
    uwsgi --stop "${PID_FILE}"; 
    notice "rm -rf ${PID_FILE}";
    rm -rf "${PID_FILE}";
}

##
## --------------------------------------------------------------------------
## 

modestop () {
    noticeall;
    if [ -f "${PID_FILE}" ]; then
        do_stop;
    else
        warn "No ${PID_FILE}";
    fi;
}

modereload() {
    noticeall;
    if [ -f "${PID_FILE}" ]; then
        do_reload;
    else
        notice "No ${PID_FILE}, so start";
        do_start;
    fi;
}

modestart () {
    noticeall;
    if [ -f "${PID_FILE}" ]; then
        warn "Already started, so restart ${PID_FILE}";
        do_stop;
        ## Time for stoping all processes.
        notice "Already started, so ... ";
        sleep 5;
        notice "... restart ${PID_FILE}"
    fi;
    do_start;
}


##
## --------------------------------------------------------------------------
## 

_ARGS=$(getopt -o hsSrv -l "help,start,stop,reload,verbose" -n $0 --  "$@");
set -- $_ARGS;

MODE="start";
VERBOSE="no";

while [[ -n $_ARGS ]] ;
do
    case $1 in
        -h|--help)      show_usage;;
        -s|--start)     MODE="start";   shift;;
        -S|--stop)      MODE="stop";    shift;;
        -r|--reload)    MODE="reload";  shift;;
        -v|--verbose)   VERBOSE="yes";  shift;;
        '--')                           break;;
        *)              wrong_usage "Unknown parameter '$1'.";;
    esac;
done;

notice "VERBOSE = ${VERBOSE}";
notice "MODE    = ${MODE}";

case "${MODE}" in
    "start"  )  modestart ;;
    "stop"   )  modestop  ;;
    "reload" )  modereload;;
    '')         error "WTF? MODE = ${MODE}";;
esac;


