var app = new Vue({
    el: '#vuejscrudapp',
    data: {
        idCita: '',
        IdPaciente: '',
        IdSchedule: '',
        citas: [],
        eidCita: '',
        eIdPaciente: '',
        eIdSchedule: '',
        cita: {}
    },
    methods: {
        showModal(id) {
            this.$refs[id].show()
        },

        hideModal(id) {
            this.$refs[id].hide()
        },

        getCitas() {
            axios.get('http://127.0.0.1:5000/citas')
                .then(response => {
                    console.log(response)
                    this.citas = response.data.Citas
                })
                .catch(error => {
                    console.log(error)
                })
        },

        onSubmit() {
            axios.get('http://127.0.0.1:5000/paciente/${this.IdPaciente}')
            axios.get('http://127.0.0.1:5000/schedule/${this.IdSchedule}')
            axios.post('http://127.0.0.1:5000/cita', {
              IdPaciente: this.IdPaciente,
              IdSchedule: this.IdSchedule
            })
            .then(response => {
              console.log(response)
              alert("Cita agregado")
              app.hideModal('Agregar')
              app.getCitas()
            })
            .catch(error => {
              console.log(error)
            })
        },

        editCita(idCita, IdPaciente, IdSchedule) {
          axios.get('http://127.0.0.1:5000/cita/' + idCita)
            .then(response => {
              this.eidCita = idCita;
              this.IdPaciente = IdPaciente;
              this.IdSchedule = IdSchedule;
              app.showModal('Editar')
            })
            .catch(error => {
              console.log(error);
            });
        },

        onUpdate() {
          const url = 'http://127.0.0.1:5000/cita/' + this.eidCita;

          axios.put(url,{
            IdPaciente: this.IdPaciente,
            IdSchedule: this.IdSchedule
          })
          .then(res => {
            console.log(res);
            alert('Cita actualizada');
            this.hideModal('Editar');
            this.getCitas();
          })
          .catch(err => {
            console.log(err);
          });
        },
    },
    mounted() {
        this.getCitas()
    }
})