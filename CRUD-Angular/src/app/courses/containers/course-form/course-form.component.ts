import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { NonNullableFormBuilder } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ErrorDialogComponent } from 'src/app/shared/components/error-dialog/error-dialog.component';
import { CoursesService } from '../../services/courses.service';

@Component({
  selector: 'app-course-form',
  templateUrl: './course-form.component.html',
  styleUrls: ['./course-form.component.scss']
})
export class CourseFormComponent implements OnInit {

  public form = this.formBiulder.group({
    name: [''],
    category: [''],
    duration: ['']
  });

  constructor(
    private formBiulder: NonNullableFormBuilder,
    private service: CoursesService,
    private dialog: MatDialog,
    private _snackBar: MatSnackBar,
    private location: Location
  ) {
  }

  onSubmit() {
    this.service.save(this.form.value).subscribe(
      resultado => { console.log(resultado); this.onSave() },
      erro => { console.error(erro); this.onError() },
      () => console.log('Fim do cíclo')
    );

  }

  onCancel(): void { 
    this.location.back();
    console.log("cancel")
  };

  onSave( ) {
    this._snackBar.open("Sucesso ao salvar curso", "close",{
      panelClass: "snackbar",
      
    });
    this.onCancel();
  }
  // console.log("SuccesMsg")

  onError() {
    this.dialog.open(ErrorDialogComponent, {
      data: "Erro ao salvar Curso! Contate o Support.",
    })
    // console.log("MsgError")
  }


  ngOnInit(): void { console.log(this.form.value.duration) };

}
